Summary:	Mounts and unmounts file systems
Summary(pl):	Montuje i odmontowuje systemy plik�w
Name:		wmmount
Version:	1.0
Release:	5
License:	GPL
Group:		X11/Window Managers/Tools
Source0:	http://www.geocities.com/SiliconValley/Vista/2471/%{name}.tgz
# Source0-md5:	f77926476c52cda5e52deb731784341a
Source1:	%{name}.desktop
Patch0:		%{name}-conf.patch
Patch1:		%{name}-ComplexProgramTargetNoMan.patch
Patch2:		%{name}-g++.patch
BuildRequires:	XFree86-devel
Requires(post):	/bin/awk
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a little application that sits in your WindowMaker's Dock and
allows you to automatically mount (and unmount) pre-defined mount
points and launch your favorite (pre-defined) file manager when you
double click on the drive icon.

%description -l pl
Dokowalna aplikacja dla WindowMakera, kt�ra pozwala na automatyczne
montowanie (i odmontowywanie) zdefiniowanych punkt�w montowania oraz
na uruchomienie ulubionego zarz�dcy plik�w przez dwukrotne klikni�cie
na ikon� nap�du.

%prep
%setup -q -n %{name}
%patch0 -p0
%patch1 -p1
%patch2 -p1

%build
xmkmf
%{__make} \
	CXXDEBUGFLAGS="%{rpmcflags}" \
	CXX=%{__cc}
touch system.wmmount

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/%{name}/icons} \
	$RPM_BUILD_ROOT%{_desktopdir}/docklets

install %{name} $RPM_BUILD_ROOT%{_bindir}

install EXTRAS/* $RPM_BUILD_ROOT%{_datadir}/%{name}/icons
install system.wmmount.awk $RPM_BUILD_ROOT%{_datadir}/%{name}
install system.wmmount $RPM_BUILD_ROOT%{_datadir}/%{name}
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}/docklets

%clean
rm -rf $RPM_BUILD_ROOT

%post
umask 022
cd %{_datadir}/%{name}
./system.wmmount.awk > system.wmmount

%files
%defattr(644,root,root,755)
%doc README system.wmmount.eg home.wmmount.eg
%attr(755,root,root) %{_bindir}/%{name}

%dir %{_datadir}/%{name}
%attr(755,root,root) %{_datadir}/%{name}/system.wmmount.awk
%config %verify(not size mtime md5) %{_datadir}/%{name}/system.wmmount

%{_datadir}/%{name}/icons
%{_desktopdir}/docklets/wmmount.desktop
