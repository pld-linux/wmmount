Summary:	Mounts and unmounts file systems
Summary(pl):	Montuje i odmontowuje systemy plików
Name:		wmmount
Version:	1.0
Release:	4
License:	GPL
Group:		X11/Window Managers/Tools
Source0:	http://www.geocities.com/SiliconValley/Vista/2471/%{name}.tgz
Source1:	%{name}.desktop
Patch0:		%{name}-conf.patch
Patch1:		%{name}-ComplexProgramTargetNoMan.patch
BuildRequires:	XFree86-devel
Prereq:		/bin/awk
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
This is a little application that sits in your WindowMaker's Dock and
allows you to automatically mount (and unmount) pre-defined mount
points and launch your favorite (pre-defined) file manager when you
double click on the drive icon.

%description -l pl
Dokowalna aplikacja dla WindowMakera, która pozwala na automatyczne
montowanie (i odmontowywanie) zdefiniowanych punktów montowania oraz
na uruchomienie ulubionego zarz±dcy plików przez dwukrotne klikniêcie
na ikonê napêdu.

%prep
%setup -q -n %{name}
%patch0 -p0
%patch1 -p1

%build

xmkmf
%{__make} \
	CXXDEBUGFLAGS="%{rpmcflags}" \
	CXX=%{__cc}
touch system.wmmount

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/%{name}/icons} \
	$RPM_BUILD_ROOT%{_applnkdir}/DockApplets

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install EXTRAS/* $RPM_BUILD_ROOT%{_datadir}/%{name}/icons
install system.wmmount.awk $RPM_BUILD_ROOT%{_datadir}/%{name}
install system.wmmount $RPM_BUILD_ROOT%{_datadir}/%{name}
#install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/DockApplets

%post
cd %{_datadir}/%{name}
./system.wmmount.awk > system.wmmount

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README system.wmmount.eg home.wmmount.eg
%attr(755,root,root) %{_bindir}/%{name}

%dir %{_datadir}/%{name}
%attr(755,root,root) %{_datadir}/%{name}/system.wmmount.awk
%config %{_datadir}/%{name}/system.wmmount

%{_datadir}/%{name}/icons

#%{_applnkdir}/DockApplets/wmmount.desktop
