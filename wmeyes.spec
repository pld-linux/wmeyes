Summary:	wmeyes - Xeyes for WindowMaker Dock
Summary(pl):	wmeyes - Xeyes dla Doku WIndowMakera
Name:		wmeyes
Version: 	1.0
Release:	3
Copyright:	GPL
Group:		X11/Window Managers/Tools
Group(pl):	X11/Zarz�dcy Okien/Narz�dzia
URL:		http://home.istar.ca/~jenora/wmeyes.html
Source0:	%{name}.tgz
Source1:	wmeyes.desktop
BuildRequires:	XFree86-devel
BuildRequires:	xpm-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define 	_prefix		/usr/X11R6

%description
wmeyes is the Xeyes for WindowMaker. It sits in the dock, 
and a pair of eyes track your cursor.

%description -l pl
wmeyes to program oparty na Xeyes, napisany z przeznaczeniem
dla Doku WindowMakera. Para oczu �ledzi ruchy kursora myszy.

%prep
%setup -q -c -n %{name}

%build
xmkmf
make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_applnkdir}/DockApplets

make install DESTDIR=$RPM_BUILD_ROOT 
install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/DockApplets

strip $RPM_BUILD_ROOT%{_bindir}/*

gzip -9nf README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.gz
%attr(755,root,root) %{_bindir}/%{name}

%{_applnkdir}/DockApplets/wmeyes.desktop
