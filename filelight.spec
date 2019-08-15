#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xDBD2CE893E2D1C87 (cfeck@kde.org)
#
Name     : filelight
Version  : 19.08.0
Release  : 12
URL      : https://download.kde.org/stable/applications/19.08.0/src/filelight-19.08.0.tar.xz
Source0  : https://download.kde.org/stable/applications/19.08.0/src/filelight-19.08.0.tar.xz
Source1 : https://download.kde.org/stable/applications/19.08.0/src/filelight-19.08.0.tar.xz.sig
Summary  : View disk usage information
Group    : Development/Tools
License  : GFDL-1.2 GPL-2.0
Requires: filelight-bin = %{version}-%{release}
Requires: filelight-data = %{version}-%{release}
Requires: filelight-license = %{version}-%{release}
Requires: filelight-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : qtbase-dev mesa-dev

%description
# Filelight
Filelight allows you to understand exactly where your diskspace is being used by
graphically representating your filesystem as a set of concentric
segmented-rings.

%package bin
Summary: bin components for the filelight package.
Group: Binaries
Requires: filelight-data = %{version}-%{release}
Requires: filelight-license = %{version}-%{release}

%description bin
bin components for the filelight package.


%package data
Summary: data components for the filelight package.
Group: Data

%description data
data components for the filelight package.


%package doc
Summary: doc components for the filelight package.
Group: Documentation

%description doc
doc components for the filelight package.


%package license
Summary: license components for the filelight package.
Group: Default

%description license
license components for the filelight package.


%package locales
Summary: locales components for the filelight package.
Group: Default

%description locales
locales components for the filelight package.


%prep
%setup -q -n filelight-19.08.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1565891224
mkdir -p clr-build
pushd clr-build
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake ..
make  %{?_smp_mflags} VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1565891224
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/filelight
cp COPYING %{buildroot}/usr/share/package-licenses/filelight/COPYING
cp COPYING-DOCS %{buildroot}/usr/share/package-licenses/filelight/COPYING-DOCS
pushd clr-build
%make_install
popd
%find_lang filelight

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/filelight

%files data
%defattr(-,root,root,-)
/usr/share/applications/org.kde.filelight.desktop
/usr/share/icons/hicolor/128x128/apps/filelight.png
/usr/share/icons/hicolor/16x16/apps/filelight.png
/usr/share/icons/hicolor/22x22/apps/filelight.png
/usr/share/icons/hicolor/32x32/apps/filelight.png
/usr/share/icons/hicolor/48x48/apps/filelight.png
/usr/share/icons/hicolor/64x64/apps/filelight.png
/usr/share/kxmlgui5/filelight/filelightui.rc
/usr/share/metainfo/org.kde.filelight.appdata.xml
/usr/share/qlogging-categories5/filelight.categories
/usr/share/xdg/filelightrc

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/HTML/de/filelight/config_appear.png
/usr/share/doc/HTML/de/filelight/config_scan.png
/usr/share/doc/HTML/de/filelight/index.cache.bz2
/usr/share/doc/HTML/de/filelight/index.docbook
/usr/share/doc/HTML/de/filelight/radial_map.png
/usr/share/doc/HTML/de/filelight/radial_map_context_menu.png
/usr/share/doc/HTML/en/filelight/config_appear.png
/usr/share/doc/HTML/en/filelight/config_scan.png
/usr/share/doc/HTML/en/filelight/index.cache.bz2
/usr/share/doc/HTML/en/filelight/index.docbook
/usr/share/doc/HTML/en/filelight/radial_map.png
/usr/share/doc/HTML/en/filelight/radial_map_context_menu.png
/usr/share/doc/HTML/es/filelight/index.cache.bz2
/usr/share/doc/HTML/es/filelight/index.docbook
/usr/share/doc/HTML/et/filelight/index.cache.bz2
/usr/share/doc/HTML/et/filelight/index.docbook
/usr/share/doc/HTML/fr/filelight/index.cache.bz2
/usr/share/doc/HTML/fr/filelight/index.docbook
/usr/share/doc/HTML/it/filelight/index.cache.bz2
/usr/share/doc/HTML/it/filelight/index.docbook
/usr/share/doc/HTML/nl/filelight/index.cache.bz2
/usr/share/doc/HTML/nl/filelight/index.docbook
/usr/share/doc/HTML/pt/filelight/index.cache.bz2
/usr/share/doc/HTML/pt/filelight/index.docbook
/usr/share/doc/HTML/pt_BR/filelight/config_appear.png
/usr/share/doc/HTML/pt_BR/filelight/config_scan.png
/usr/share/doc/HTML/pt_BR/filelight/index.cache.bz2
/usr/share/doc/HTML/pt_BR/filelight/index.docbook
/usr/share/doc/HTML/pt_BR/filelight/radial_map.png
/usr/share/doc/HTML/pt_BR/filelight/radial_map_context_menu.png
/usr/share/doc/HTML/ru/filelight/index.cache.bz2
/usr/share/doc/HTML/ru/filelight/index.docbook
/usr/share/doc/HTML/sv/filelight/index.cache.bz2
/usr/share/doc/HTML/sv/filelight/index.docbook
/usr/share/doc/HTML/uk/filelight/config_appear.png
/usr/share/doc/HTML/uk/filelight/config_scan.png
/usr/share/doc/HTML/uk/filelight/index.cache.bz2
/usr/share/doc/HTML/uk/filelight/index.docbook
/usr/share/doc/HTML/uk/filelight/radial_map.png
/usr/share/doc/HTML/uk/filelight/radial_map_context_menu.png

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/filelight/COPYING
/usr/share/package-licenses/filelight/COPYING-DOCS

%files locales -f filelight.lang
%defattr(-,root,root,-)

