Summary:	wmeyes - Xeyes for WindowMaker Dock
Summary(pl):	wmeyes - Xeyes dla Doku WindowMakera
Summary(pt_BR):	xeyes para o WindowMaker
Summary(es):	xeyes para WindowMaker
Name:		wmeyes
Version:	1.0
Release:	3
License:	GPL
Group:		X11/Window Managers/Tools
Source0:	http://home.istar.ca/~jenora/%{name}.tgz
Source1:	%{name}.desktop
Patch0:		%{name}-sigalarm.patch
Patch1:		%{name}-ComplexProgramTargetNoMan.patch
URL:		http://home.istar.ca/~jenora/wmeyes.html
BuildRequires:	XFree86-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define 	_prefix		/usr/X11R6

%description
wmeyes is the Xeyes for WindowMaker. It sits in the dock, and a pair
of eyes track your cursor.

%description -l pl
wmeyes to program oparty na Xeyes, napisany z przeznaczeniem dla Doku
WindowMakera. Para oczu ¶ledzi ruchy kursora myszy.

%description -l pt_BR
O wmeyes é uma implementação do xeyes clássico do X Window System,
para o WindowMaker. Agora você nunca mais perderá o seu ponteiro do
mouse de novo.

%description -l es
xeyes para WindowMaker

%prep
%setup -q -c -n %{name}
%patch0 -p1
%patch1 -p1

%build
xmkmf -a
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_applnkdir}/DockApplets

%{__make} install DESTDIR=$RPM_BUILD_ROOT
#install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/DockApplets


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/%{name}

#%{_applnkdir}/DockApplets/wmeyes.desktop
