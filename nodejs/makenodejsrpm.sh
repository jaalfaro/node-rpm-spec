#!/bin/bash
VERSION=v0.10.22

rm -Rf ~/rpmbuild
mkdir -p ~/rpmbuild/BUILD ~/rpmbuild/RPMS ~/rpmbuild/RPMS/i386 ~/rpmbuild/RPMS/noarch ~/rpmbuild/RPMS/x86_64 ~/rpmbuild/RPMS/ ~/rpmbuild/SOURCES ~/rpmbuild/SPECS ~/rpmbuild/SRPMS
echo '%_topdir %(echo $HOME)/rpmbuild' >> ~/.rpmmacros
wget -P ~/rpmbuild/SOURCES http://nodejs.org/dist/$VERSION/node-$VERSION.tar.gz
wget -P ~/rpmbuild/SPECS https://raw.github.com/jaalfaro/node-rpm-spec/master/nodejs.spec
rpmbuild -ba ~/rpmbuild/SPECS/nodejs.spec
rm ~/.rpmmacros