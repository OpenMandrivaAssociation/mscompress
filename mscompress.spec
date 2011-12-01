Summary:	MS compress/expand-compatible (de)compressor
Summary(pl):	(De)kompresor zgodny z MS compress/expand
Name:		mscompress
Version:	0.3
Release:	%mkrel 13
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
rm -rf %{buildroot}
install -d %{buildroot}{%{_bindir},%{_mandir}/man1}

install mscompress msexpand %{buildroot}%{_bindir}
install mscompress.1 msexpand.1 %{buildroot}%{_mandir}/man1

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc ChangeLog README TODO format.txt
%{_bindir}/*
%{_mandir}/man1/*

