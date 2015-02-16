#-
# Copyright 2014 Emmanuel Vadot <elbarto@bocal.org>
# All rights reserved
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted providing that the following conditions 
# are met:
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE AUTHOR ``AS IS'' AND ANY EXPRESS OR
# IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED.  IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS
# OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
# HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT,
# STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING
# IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

Name:           patterns-BLINUX-epitech-exam
Version:        2.0
Release:        4
Summary:        Meta package for Epitech Exam need
Group:          Metapackages
License:        BSD-2-Clause
Url:            http://www.blinux.fr
BuildRequires:  patterns
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

Requires:	autoconf
Requires:	automake
Requires:	binutils
Requires:	cmake
Requires:	gcc
Requires:	gcc-32bit
Requires:	gcc-c++
Requires:	gcc-c++-32bit
Requires:	gd
Requires:	gdb
Requires:	gdbserver
Requires:	htop
Requires:	llvm-clang
Requires:	ltrace
Requires:	make
Requires:	mariadb
Requires:	mariadb-client
Requires:	most
Requires:	nano
Requires:	nasm
Requires:	ocaml
Requires:	php5
Requires:	php5-gd
Requires:	php5-gettext
Requires:	php5-mbstring
Requires:	php5-mysql
Requires:	php5-mcrypt
Requires:	php5-phar
Requires:	php5-posix
Requires:	rlwrap
Requires:	sqlite2
Requires:	sqlite2-devel
Requires:	terminator
Requires:	texlive-latex
Requires:	texlive-pdftex
Requires:	texlive-pdftools
Requires:	tree
Requires:	valgrind
Requires:	zip
Requires:	zlib-devel
Requires:	zsh

%description
This is a meta-package for the needs for EPITECH in BLINUX EXAM

%prep

%build

%install

%files
