%global npm_name supervisor

Summary:       A supervisor program for running nodejs programs
Name:          nodejs-%{npm_name}
Version:       0.5.5
Release:       3%{?dist}
Group:         System Environment/Libraries
License:       MIT
URL:           https://github.com/isaacs/node-supervisor
Source0:       http://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
# They have added a LICENSE file, but not updated the package
# We are including their LICENSE file until the next version, when
#   the file should be in the tarball
# https://raw.github.com/isaacs/node-supervisor/master/LICENSE
SOURCE1:       nodejs-supervisor-LICENSE
BuildRequires: nodejs-devel
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

cp -pr %{SOURCE1} LICENSE

%build
#nothing to do

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pr lib package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}

# Setup Binaries
mkdir %{buildroot}%{_bindir}
ln -s %{nodejs_sitelib}/%{npm_name}/lib/cli-wrapper.js %{buildroot}%{_bindir}/node-supervisor
ln -s %{nodejs_sitelib}/%{npm_name}/lib/cli-wrapper.js %{buildroot}%{_bindir}/supervisor

# Create man pages
mkdir -p %{buildroot}%{_mandir}/man1
%{buildroot}%{nodejs_sitelib}/%{npm_name}/lib/cli-wrapper.js -h > helpfile
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

