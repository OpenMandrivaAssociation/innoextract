Name:           innoextract
Version:        1.7
Release:        1
License:        zlib
Summary:        A tool to unpack "exe" installers created by Inno Setup
Url:            http://constexpr.org/innoextract/
Group:          Archiving/Compression
Source:         http://constexpr.org/innoextract/files/%{name}-%{version}/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  boost-devel
BuildRequires:  pkgconfig(liblzma)

%description
Inno Setup is a tool to create installers for Microsoft Windows
applications. innoextract allows to extract such installers under
non-windows systems without running the actual installer using wine.

%prep
%setup -q

%build
%cmake
%make_build

%install
%make_install -C build

%files
%doc README.md CHANGELOG VERSION LICENSE
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.xz
