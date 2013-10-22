node rpm specfile
=================
Node.js does not come with RPMs for CentOS 5.9. Here are instructions to build node rpms from source.

Steps to build
--------------------------------------------------------
1. sudo yum groupinstall 'Development Tools'
2. sudo yum install openssl-devel python26
3. /usr/sbin/useradd makerpm #Never build as root.
4. usermod -a -G mock makerpm
5. passwd makerpm
6. su - makerpm
7. ./makenodejsrpm.sh
