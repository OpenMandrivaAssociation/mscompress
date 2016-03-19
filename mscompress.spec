Summary:	MS compress/expand-compatible (de)compressor
Name:		mscompress
Version:	0.4
Release:	10
License:	GPL
Group:		Archiving/Compression
Url:        ftp://ftp.penguin.cz/pub/users/mhi/mscompress
Source0:	http://code.stapelberg.de/git/mscompress/snapshot/%{name}-%{version}.tar.bz2
BuildRequires:	autoconf

%description
Microsoft compress.exe/expand.exe-compatible file (de)compressor.

%prep
%setup -q

%build
./autogen.sh
%configure2_5x
%make

%install
%makeinstall_std

%files
%doc ChangeLog README TODO format.txt
%{_bindir}/*
%{_mandir}/man1/*

