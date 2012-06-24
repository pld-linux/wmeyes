Summary:	wmeyes - Xeyes for WindowMaker Dock
Summary(pl):	wmeyes - Xeyes dla Doku WindowMakera
Summary(pt_BR):	xeyes para o WindowMaker
Summary(es):	xeyes para WindowMaker
Name:		wmeyes
Version:	1.2
Release:	1
License:	MIT
Group:		X11/Window Managers/Tools
Source0:	http://www.bstern.org/wmeyes/%{name}-%{version}.tar.gz
# Source0-md5:	bb687b5fea83d49b35552a181083142b
Source1:	%{name}.desktop
Patch0:		%{name}-ComplexProgramTargetNoMan.patch
URL:		http://www.bstern.org/wmeyes/
BuildRequires:	XFree86-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
wmeyes is the Xeyes for WindowMaker. It sits in the dock, and a pair
of eyes track your cursor.

%description -l pl
wmeyes to program oparty na Xeyes, napisany z przeznaczeniem dla Doku
WindowMakera. Para oczu �ledzi ruchy kursora myszy.

%description -l pt_BR
O wmeyes � uma implementa��o do xeyes cl�ssico do X Window System,
para o WindowMaker. Agora voc� nunca mais perder� o seu ponteiro do
mouse de novo.

%description -l es
xeyes para WindowMaker

%prep
%setup -q 
%patch0 -p1

%build
xmkmf -a
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_desktopdir}/docklets \
	$RPM_BUILD_ROOT%{_bindir}

install %{name} $RPM_BUILD_ROOT%{_bindir}
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}/docklets

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{_bindir}/%{name}
%{_desktopdir}/docklets/wmeyes.desktop
