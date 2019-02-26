#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x393587D97D86500B (cjwatson@debian.org)
#
Name     : man-db
Version  : 2.8.5
Release  : 34
URL      : http://nongnu.askapache.com/man-db/man-db-2.8.5.tar.xz
Source0  : http://nongnu.askapache.com/man-db/man-db-2.8.5.tar.xz
Source99 : http://nongnu.askapache.com/man-db/man-db-2.8.5.tar.xz.asc
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0 GPL-2.0+ GPL-3.0+ LGPL-2.1
Requires: man-db-bin = %{version}-%{release}
Requires: man-db-config = %{version}-%{release}
Requires: man-db-data = %{version}-%{release}
Requires: man-db-lib = %{version}-%{release}
Requires: man-db-libexec = %{version}-%{release}
Requires: man-db-license = %{version}-%{release}
Requires: man-db-locales = %{version}-%{release}
Requires: man-db-man = %{version}-%{release}
Requires: man-db-services = %{version}-%{release}
Requires: groff
BuildRequires : automake
BuildRequires : automake-dev
BuildRequires : flex
BuildRequires : gdbm-dev
BuildRequires : gettext-bin
BuildRequires : glibc-locale
BuildRequires : groff
BuildRequires : less
BuildRequires : libpipeline-dev
BuildRequires : libseccomp-dev
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
Requires: man-db-data = %{version}-%{release}
Requires: man-db-libexec = %{version}-%{release}
Requires: man-db-config = %{version}-%{release}
Requires: man-db-license = %{version}-%{release}
Requires: man-db-services = %{version}-%{release}

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
Requires: man-db-man = %{version}-%{release}

%description doc
doc components for the man-db package.


%package lib
Summary: lib components for the man-db package.
Group: Libraries
Requires: man-db-data = %{version}-%{release}
Requires: man-db-libexec = %{version}-%{release}
Requires: man-db-license = %{version}-%{release}

%description lib
lib components for the man-db package.


%package libexec
Summary: libexec components for the man-db package.
Group: Default
Requires: man-db-config = %{version}-%{release}
Requires: man-db-license = %{version}-%{release}

%description libexec
libexec components for the man-db package.


%package license
Summary: license components for the man-db package.
Group: Default

%description license
license components for the man-db package.


%package locales
Summary: locales components for the man-db package.
Group: Default

%description locales
locales components for the man-db package.


%package man
Summary: man components for the man-db package.
Group: Default

%description man
man components for the man-db package.


%package services
Summary: services components for the man-db package.
Group: Systemd services

%description services
services components for the man-db package.


%prep
%setup -q -n man-db-2.8.5
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1551154952
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
export SOURCE_DATE_EPOCH=1551154952
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/man-db
cp docs/COPYING %{buildroot}/usr/share/package-licenses/man-db/docs_COPYING
cp docs/COPYING.LIB %{buildroot}/usr/share/package-licenses/man-db/docs_COPYING.LIB
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

%files config
%defattr(-,root,root,-)
/usr/lib/tmpfiles.d/man-db.conf

%files data
%defattr(-,root,root,-)
/usr/share/defaults/mandb/man_db.conf

%files doc
%defattr(0644,root,root,0755)
%doc /usr/share/doc/man\-db/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/man-db/libman-2.8.5.so
/usr/lib64/man-db/libman.so
/usr/lib64/man-db/libmandb-2.8.5.so
/usr/lib64/man-db/libmandb.so

%files libexec
%defattr(-,root,root,-)
/usr/libexec/man-db/globbing
/usr/libexec/man-db/manconv
/usr/libexec/man-db/zsoelim

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/man-db/docs_COPYING
/usr/share/package-licenses/man-db/docs_COPYING.LIB

%files man
%defattr(0644,root,root,0755)
/usr/share/man/it/man1/apropos.1
/usr/share/man/it/man1/man.1
/usr/share/man/it/man1/manpath.1
/usr/share/man/it/man1/whatis.1
/usr/share/man/it/man1/zsoelim.1
/usr/share/man/it/man5/manpath.5
/usr/share/man/it/man8/accessdb.8
/usr/share/man/it/man8/catman.8
/usr/share/man/it/man8/mandb.8
/usr/share/man/man1/apropos.1
/usr/share/man/man1/lexgrog.1
/usr/share/man/man1/man.1
/usr/share/man/man1/manconv.1
/usr/share/man/man1/manpath.1
/usr/share/man/man1/whatis.1
/usr/share/man/man1/zsoelim.1
/usr/share/man/man5/manpath.5
/usr/share/man/man8/accessdb.8
/usr/share/man/man8/catman.8
/usr/share/man/man8/mandb.8

%files services
%defattr(-,root,root,-)
/lib/systemd/system/man-db.service
/lib/systemd/system/man-db.timer

%files locales -f man-db-gnulib.lang -f man-db.lang
%defattr(-,root,root,-)

