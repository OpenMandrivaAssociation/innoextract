Name:           innoextract
Version:	1.9
Release:	6
License:        zlib
Summary:        A tool to unpack "exe" installers created by Inno Setup
Url:            http://constexpr.org/innoextract/
Group:          Archiving/Compression
Source0:        http://constexpr.org/innoextract/files/%{name}-%{version}/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:	ninja
BuildRequires:  boost-devel
BuildRequires:  pkgconfig(liblzma)
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(libzstd)

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
%autosetup -p1

%build
%cmake -G Ninja
%ninja_build

%install
%ninja_install -C build

%files
%doc README.md CHANGELOG VERSION LICENSE
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
