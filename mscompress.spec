Summary:	MS compress/expand-compatible (de)compressor
Summary(pl):	(De)kompresor zgodny z MS compress/expand
Name:		mscompress
Version:	0.3
Release:	%mkrel 10
License:	GPL
Group:		Archiving/Compression
Url:        ftp://ftp.penguin.cz/pub/users/mhi/mscompress
Source0:	ftp://ftp.penguin.cz/pub/users/mhi/mscompress/%{name}-%{version}.tar.bz2
Patch0:		mscompress-0.3-LDFLAGS.diff
BuildRequires:	autoconf
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Microsoft compress.exe/expand.exe-compatible file (de)compressor.

%description -l pl
Program kompresuj±cy i dekompresuj±cy zgodny z compress.exe/expand.exe
Microsoftu.

%prep
%setup -q
%patch0 -p0

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install mscompress msexpand $RPM_BUILD_ROOT%{_bindir}
install mscompress.1 msexpand.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc ChangeLog README TODO format.txt
%{_bindir}/*
%{_mandir}/man1/*

