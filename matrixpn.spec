%define		rel	2
Summary:	Short voice messages through a web
Summary(pl):	Przesy�anie kr�tkich wiadomo�ci g�osowych przez sie�
Name:		matrixpn
Version:	0.3
Release:	1
License:	GPL
Group:		Applications/Sound
Source0:	http://auriga.wearlab.de:81/matrixpn/%{name}_%{version}-%{rel}.tar.gz
URL:		http://matrixpn.auriga.wearlab.de/
BuildRequires:	gtk+-devel
BuildRequires:	libogg-devel
BuildRequires:	libvorbis-devel 
BuildRequires:	libxml2-devel
BuildRequires:	libxslt-devel 
BuildRequires:	xmms-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_xmms_path	/usr/X11R6/lib/xmms/

%description
MPN spreads short voice messages through a web of trust; credibility
decays until a threshold where the message is dropped. It comes with a
program for recording and sending messages as well as plugins for XMMS
(in separate package) and WinAmp (in Windows version) that play
received messages.
				 
%description -l pl
MPN rozpowszechnia kr�tkie wiadomo�ci g�osowe poprzez sie� zaufania;
wiarygodno�� zanika do osi�gni�cia progu, poni�ej kt�rego wiadomo��
jest porzucana. Zestaw zawiera program do nagrywania i wysy�ania
wiadomo�ci oraz wtyczki odtwarzaj�ce dla XMMS-a (w oddzielnym
pakiecie) i WinAmpa (w wersji pod Windows).

%package devel
Summary:	MPN development package
Summary(pl):	Pakiet do programowania z u�yciem MPN
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
MPN development package.

%description devel -l pl
Pakiet do programowania z u�yciem MPN.

%package -n xmms-effect-matrixnews
Summary:        MPN plugin for XMMS
Summary(pl):    Wtyczka MPN dla XMMS-a
Group:          X11/Applications/Multimedia
Requires:	%{name} = %{version}

%description -n xmms-effect-matrixnews
MPN plugin for XMMS.

%description -n xmms-effect-matrixnews -l pl
Wtyczka MPN dla XMMS-a.

%prep
%setup -q -n %{name}-%{version}

%build
rm -f missing
%{__libtoolize}
aclocal
%{__autoconf}
autoheader
%{__automake}
%configure --disable-xmltest
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README ChangeLog GETTINGSTARTED SFLLICENSE.TXT AUTHORS
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}

%files devel
%defattr(644,root,root,755)
%{_includedir}/mpn
%{_libdir}/*

%files -n xmms-effect-matrixnews
%defattr(644,root,root,755)
%attr(755,root,root) %{_xmms_path}/Effect/*