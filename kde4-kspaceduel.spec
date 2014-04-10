%define		_state		stable
%define		orgname		kspaceduel
%define		qtver		4.8.0

Summary:	KDE space arcade game for two players
Summary(pl.UTF-8):	Gra zręcznościowa pod KDE dla dwóch graczy
Summary(pt_BR.UTF-8):	Versão do jogo Duelo Espacial para o KDE
Name:		kde4-%{orgname}
Version:	4.12.4
Release:	1
License:	GPL
Group:		X11/Applications/Games
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/%{orgname}-%{version}.tar.xz
# Source0-md5:	baaba65b05b8ba54c9b8560073a0652a
BuildRequires:	automoc4 >= 0.9.88
BuildRequires:	cmake >= 2.8.0
BuildRequires:	kde4-kdelibs-devel >= %{version}
BuildRequires:	kde4-libkdegames-devel >= %{version}
BuildRequires:	qt4-build >= %{qtver}
BuildRequires:	qt4-qmake >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.600
Obsoletes:	kde4-kdegames-%{orgname}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Each player control a ship that flies around the sun and tries to
shoot at the other ship. You can play KSpaceduel with another person,
against the computer, or you can have the computer control both ships
and play each other.

%description -l pl.UTF-8
Każdy z graczy kieruje statkiem, który lata dookoła słońca i próbuje
zestrzelić drugi statek. Można grać w KSpaceduel z inną osobą, z
komputerem, lub pozwolić, aby komputer kierował obydwoma statkami.

%description -l pt_BR.UTF-8
Versão do jogo Duelo Espacial para o KDE.

%prep
%setup -q -n %{orgname}-%{version}

%build
install -d build
cd build
%cmake \
	../

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

install -d $RPM_BUILD_ROOT/var/games
# remove locolor icons
rm -rf $RPM_BUILD_ROOT%{_iconsdir}/locolor

%find_lang %{orgname}	--with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{orgname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kspaceduel
%{_desktopdir}/kde4/kspaceduel.desktop
%{_datadir}/apps/kspaceduel
%{_datadir}/config.kcfg/kspaceduel.kcfg
%{_iconsdir}/*/*/apps/kspaceduel.png
