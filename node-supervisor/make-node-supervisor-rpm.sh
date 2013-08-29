#!/bin/bash
VERSION=0.5.5

rm -Rf ~/rpmbuild
mkdir -p ~/rpmbuild/BUILD ~/rpmbuild/RPMS ~/rpmbuild/RPMS/i386 ~/rpmbuild/RPMS/noarch ~/rpmbuild/RPMS/x86_64 ~/rpmbuild/RPMS/ ~/rpmbuild/SOURCES ~/rpmbuild/SPECS ~/rpmbuild/SRPMS
echo '%_topdir %(echo $HOME)/rpmbuild' >> ~/.rpmmacros
wget -P ~/rpmbuild/SOURCES http://registry.npmjs.org/supervisor/-/supervisor-$VERSION.tgz
wget -P ~/rpmbuild/SPECS https://raw.github.com/jaalfaro/node-rpm-spec/master/node-supervisor/nodejs-supervisor.spec
rpmbuild -ba ~/rpmbuild/SPECS/nodejs-supervisor.spec
rm ~/.rpmmacros