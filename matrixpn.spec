#
# TODO:
# Summaries, descriptions,
#
%define		rel	2
Summary:	Short voice messages through a web.
Summary(pl):	-
Name:		matrixpn
Version:	0.3
Release:	1
License:	GPL
Group:		-
Source0:	http://auriga.wearlab.de:81/matrixpn/%{name}_%{version}-%{rel}.tar.gz
URL:		http://matrixpn.auriga.wearlab.de/
BuildRequires:	gtk+-devel
BuildRequires:	libogg-devel
BuildRequires:	libvorbis-devel 
BuildRequires:	libxml2-devel
BuildRequires:	libxslt-devel 
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
%define		_xmms_path	/usr/X11R6/lib/xmms/

%description

%description -l pl

%package devel
Summary:	-
Summary(pl):	-
Group:		-
Requires:	%{name} = %{version}

%description devel

%description devel -l pl

%package -n xmms-effect-matrixnews
Summary:        -
Summary(pl):    -
Group:          -
BuildRequires:	xmms-devel
Requires:	%{name} = %{version}

%description -n xmms-effect-matrixnews

%description -n xmms-effect-matrixnews -l pl

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
%{_includedir}/mpn/
%{_libdir}/

%files -n xmms-effect-matrixnews
%defattr(644,root,root,755)
%{_xmms_path}/Effect
