Name:           innoextract
Version:        1.7
Release:        2
License:        zlib
Summary:        A tool to unpack "exe" installers created by Inno Setup
Url:            http://constexpr.org/innoextract/
Group:          Archiving/Compression
Source0:        http://constexpr.org/innoextract/files/%{name}-%{version}/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  boost-devel
BuildRequires:  pkgconfig(liblzma)

%description
Inno Setup is a tool to create installers for Microsoft Windows
applications. innoextract allows to extract such installers under
non-windows systems without running the actual installer using wine.

#USAGE
#Run
#
#To extract a setup file to the current directory run:
#
#$ innoextract <file>
#
#A list of available options can be retrieved using
#
#$ innoextract --help
#
#Documentation is also available as a man page:
#
#$ man 1 innoextract

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
