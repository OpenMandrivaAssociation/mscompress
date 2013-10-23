Summary:	MS compress/expand-compatible (de)compressor
Name:		mscompress
Version:	0.3
Release:	17
License:	GPLv2
Group:		Archiving/Compression
Url:		ftp://ftp.penguin.cz/pub/users/mhi/mscompress
Source0:	ftp://ftp.penguin.cz/pub/users/mhi/mscompress/%{name}-%{version}.tar.bz2
Patch0:		mscompress-0.3-LDFLAGS.diff

%description
Microsoft compress.exe/expand.exe-compatible file (de)compressor.

%prep
%setup -q
%patch0 -p0

%build
%configure2_5x
%make

%install
install -d %{buildroot}{%{_bindir},%{_mandir}/man1}

install mscompress msexpand %{buildroot}%{_bindir}
install mscompress.1 msexpand.1 %{buildroot}%{_mandir}/man1

%files
%doc ChangeLog README TODO format.txt
%{_bindir}/*
%{_mandir}/man1/*

