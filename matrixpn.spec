%define		rel	2
Summary:	Short voice messages through a web
Summary(pl.UTF-8):	Przesyłanie krótkich wiadomości głosowych przez sieć
Name:		matrixpn
Version:	0.3
Release:	2
License:	GPL
Group:		Applications/Sound
Source0:	http://download.auriga.wearlab.de/matrixpn/%{name}_%{version}-%{rel}.tar.gz
# Source0-md5:	4177a281945aa6442177b69303a04cc1
URL:		http://matrixpn.auriga.wearlab.de/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+-devel
BuildRequires:	libogg-devel
BuildRequires:	libtool
BuildRequires:	libvorbis-devel
BuildRequires:	libxml2-devel
BuildRequires:	libxslt-devel
BuildRequires:	rpmbuild(macros) >= 1.125
BuildRequires:	xmms-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
MPN spreads short voice messages through a web of trust; credibility
decays until a threshold where the message is dropped. It comes with a
program for recording and sending messages as well as plugins for XMMS
(in separate package) and WinAmp (in Windows version) that play
received messages.

%description -l pl.UTF-8
MPN rozpowszechnia krótkie wiadomości głosowe poprzez sieć zaufania;
wiarygodność zanika do osiągnięcia progu, poniżej którego wiadomość
jest porzucana. Zestaw zawiera program do nagrywania i wysyłania
wiadomości oraz wtyczki odtwarzające dla XMMS-a (w oddzielnym
pakiecie) i WinAmpa (w wersji pod Windows).

%package devel
Summary:	MPN development package
Summary(pl.UTF-8):	Pakiet do programowania z użyciem MPN
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
MPN development package.

%description devel -l pl.UTF-8
Pakiet do programowania z użyciem MPN.

%package -n xmms-effect-matrixnews
Summary:	MPN plugin for XMMS
Summary(pl.UTF-8):	Wtyczka MPN dla XMMS-a
Group:		X11/Applications/Sound
Requires:	%{name} = %{version}-%{release}
Requires:	xmms

%description -n xmms-effect-matrixnews
MPN plugin for XMMS.

%description -n xmms-effect-matrixnews -l pl.UTF-8
Wtyczka MPN dla XMMS-a.

%prep
%setup -q

%build
rm -f missing
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-xmltest
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

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
%attr(755,root,root) %{xmms_effect_plugindir}/*
