#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x393587D97D86500B (cjwatson@debian.org)
#
Name     : man-db
Version  : 2.8.3
Release  : 29
URL      : http://nongnu.askapache.com/man-db/man-db-2.8.3.tar.xz
Source0  : http://nongnu.askapache.com/man-db/man-db-2.8.3.tar.xz
Source99 : http://nongnu.askapache.com/man-db/man-db-2.8.3.tar.xz.asc
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0 GPL-2.0+ GPL-3.0+ LGPL-2.1
Requires: man-db-bin
Requires: man-db-config
Requires: man-db-lib
Requires: man-db-data
Requires: man-db-doc
Requires: man-db-locales
Requires: groff
BuildRequires : automake
BuildRequires : automake-dev
BuildRequires : db-dev
BuildRequires : flex
BuildRequires : gdbm-dev
BuildRequires : gettext-bin
BuildRequires : groff
BuildRequires : less
BuildRequires : libpipeline-dev
BuildRequires : libtool
BuildRequires : libtool-dev
BuildRequires : m4
BuildRequires : pkg-config-dev
BuildRequires : util-linux
BuildRequires : zlib-dev
Patch1: stateless.patch
Patch2: cve-2015-1336.nopatch

%description
========================================
Please read the man-db manual, included in the manual subdirectory of this
distribution.  It contains configuration details and other aspects of this

%package bin
Summary: bin components for the man-db package.
Group: Binaries
Requires: man-db-data
Requires: man-db-config

%description bin
bin components for the man-db package.


%package config
Summary: config components for the man-db package.
Group: Default

%description config
config components for the man-db package.


%package data
Summary: data components for the man-db package.
Group: Data

%description data
data components for the man-db package.


%package doc
Summary: doc components for the man-db package.
Group: Documentation

%description doc
doc components for the man-db package.


%package lib
Summary: lib components for the man-db package.
Group: Libraries
Requires: man-db-data

%description lib
lib components for the man-db package.


%package locales
Summary: locales components for the man-db package.
Group: Default

%description locales
locales components for the man-db package.


%prep
%setup -q -n man-db-2.8.3
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1526011261
export CFLAGS="$CFLAGS -fstack-protector-strong -mzero-caller-saved-regs=used "
export FCFLAGS="$CFLAGS -fstack-protector-strong -mzero-caller-saved-regs=used "
export FFLAGS="$CFLAGS -fstack-protector-strong -mzero-caller-saved-regs=used "
export CXXFLAGS="$CXXFLAGS -fstack-protector-strong -mzero-caller-saved-regs=used "
%reconfigure --disable-static --disable-setuid
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1526011261
rm -rf %{buildroot}
%make_install
%find_lang man-db-gnulib
%find_lang man-db

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/accessdb
/usr/bin/apropos
/usr/bin/catman
/usr/bin/lexgrog
/usr/bin/man
/usr/bin/mandb
/usr/bin/manpath
/usr/bin/whatis
/usr/libexec/man-db/globbing
/usr/libexec/man-db/manconv
/usr/libexec/man-db/zsoelim

%files config
%defattr(-,root,root,-)
/usr/lib/tmpfiles.d/man-db.conf

%files data
%defattr(-,root,root,-)
/usr/share/defaults/mandb/man_db.conf
/usr/share/man/es/man1/apropos.1
/usr/share/man/es/man1/man.1
/usr/share/man/es/man1/manpath.1
/usr/share/man/es/man1/whatis.1
/usr/share/man/es/man1/zsoelim.1
/usr/share/man/es/man5/manpath.5
/usr/share/man/es/man8/catman.8
/usr/share/man/es/man8/mandb.8
/usr/share/man/it/man1/apropos.1
/usr/share/man/it/man1/man.1
/usr/share/man/it/man1/manpath.1
/usr/share/man/it/man1/whatis.1
/usr/share/man/it/man1/zsoelim.1
/usr/share/man/it/man5/manpath.5
/usr/share/man/it/man8/accessdb.8
/usr/share/man/it/man8/catman.8
/usr/share/man/it/man8/mandb.8

%files doc
%defattr(-,root,root,-)
%doc /usr/share/doc/man\-db/*
%doc /usr/share/man/man1/*
%doc /usr/share/man/man5/*
%doc /usr/share/man/man8/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/man-db/libman-2.8.3.so
/usr/lib64/man-db/libman.so
/usr/lib64/man-db/libmandb-2.8.3.so
/usr/lib64/man-db/libmandb.so

%files locales -f man-db-gnulib.lang -f man-db.lang
%defattr(-,root,root,-)

