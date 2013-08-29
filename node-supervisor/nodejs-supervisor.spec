%global npm_name supervisor
# nodejs binary
%define __nodejs %{_bindir}/node

# nodejs library directory
%nodejs_sitelib %{_prefix}/lib/node_modules

#arch specific library directory
#for future-proofing only; we don't do multilib
%nodejs_sitearch %{nodejs_sitelib}

# currently installed nodejs version
%nodejs_version %(%{__nodejs} -v | sed s/v//)

# symlink dependencies so `npm link` works
# this should be run in every module's %%install section
# pass --check to work in the current directory instead of the buildroot
# pass --no-devdeps to ignore devDependencies when --check is used
%nodejs_symlink_deps %{_rpmconfigdir}/nodejs-symlink-deps %{nodejs_sitelib}

# patch package.json to fix a dependency
# see `man npm-json` for details on writing dependencies for package.json files
# e.g. `%%nodejs_fixdep frobber` makes any version of frobber do
#      `%%nodejs_fixdep frobber '>1.0'` requires frobber > 1.0
#      `%%nodejs_fixdep -r frobber removes the frobber dep
%nodejs_fixdep %{_rpmconfigdir}/nodejs-fixdep

# macro to filter unwanted provides from Node.js binary native modules
%nodejs_default_filter %{expand: \
%global __provides_exclude_from ^%{nodejs_sitearch}/.*\\.node$
}

# no-op macro to allow spec compatibility with EPEL
%nodejs_find_provides_and_requires %{nil}
Summary:       A supervisor program for running nodejs programs
Name:          nodejs-%{npm_name}
Version:       0.5.5
Release:       1%{?dist}
Group:         System Environment/Libraries
License:       MIT
URL:           https://github.com/isaacs/node-supervisor
Source0:       http://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: nodejs
BuildRequires: txt2man
BuildArch:     noarch

%description
A little supervisor script for nodejs. It runs your program,
and watches for code changes, so you can have hot-code 
reloading like behavior, without worrying about memory leaks 
and making sure you clean up all the inter-module references, 
and without a whole new require system. 

%prep
%setup -q -n package

%build
#nothing to do

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pr lib package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}

# Setup Binaries
mkdir -p %{buildroot}%{_bindir}
ln -s %{nodejs_sitelib}/%{npm_name}/lib/cli-wrapper.js %{buildroot}%{_bindir}/node-supervisor
ln -s %{nodejs_sitelib}/%{npm_name}/lib/cli-wrapper.js %{buildroot}%{_bindir}/supervisor

# Create man pages
mkdir -p %{buildroot}%{_mandir}/man1
node %{buildroot}%{nodejs_sitelib}/%{npm_name}/lib/cli-wrapper.js -h > helpfile
txt2man -P node-supervisor -t node-supervisor -r %{version} helpfile > %{buildroot}%{_mandir}/man1/node-supervisor.1
txt2man -P supervisor -t supervisor -r %{version} helpfile > %{buildroot}%{_mandir}/man1/supervisor.1
rm -f helpfile

%files
%doc README.md LICENSE
%{nodejs_sitelib}/%{npm_name}
%{_bindir}/node-supervisor
%{_bindir}/supervisor
%{_mandir}/man1/*

%changelog
* Wed Aug 29 2013 John Alfaro <john@thealfaros.com> - 0.5.5-1
- Bump release number up

* Wed Jun 19 2013 Troy Dawson <tdawson@redhat.com> - 0.5.2-3
- Bump release number up (#975862)

* Tue May 28 2013 Troy Dawson <tdawson@redhat.com> - 0.5.2-2
- Fixed Summary and Description spelling errors
- Added BSD License file, from upstream
- Create man pages

* Fri Mar 01 2013 Troy Dawson <tdawson@redhat.com> - 0.5.2-1
- Update to 0.5.2
- Update spec to Fedora nodejs standards

* Wed Sep 05 2012 Troy Dawson <tdawson@redhat.com> - 0.4.1-2
- Rewored spec file using tchor template

* Wed Sep 05 2012 Troy Dawson <tdawson@redhat.com> - 0.4.1-1
- Initial build

