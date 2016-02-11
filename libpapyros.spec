%define debug_package %nil
%define snap %nil

%define major 0
%define libname %mklibname Papyros %{major}
%define devname %mklibname Papyros -d

Summary:	Papyros Libraries
Name:		libpapyros
Version:	0.2.0
Release:	1
License:	GPLv2
Group:		Graphical desktop/Other
URL:		https://github.com/papyros/libpapyros
# git clone https://github.com/papyros/libpapyros.git
# git archive --format=tar --prefix libpapyros-0.1.0-$(date +%Y%m%d)/ HEAD | xz -vf > libpapyros-0.1.0-$(date +%Y%m%d).tar.xz
Source0:	%{name}-%{version}.tar.gz
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF5Config)
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5Qml)
BuildRequires:	pkgconfig(Qt5Quick)

%description
A collection of classes used throughout Papyros

%package -n %{libname}
Summary:	Main library for %{name}
Group:		System/Libraries

%description -n %{libname}
Main library for %{name}.

%package -n %{devname}
Summary:	Development library for %{name}
Group:		Development/KDE and Qt
Requires:	%{libname} = %{EVRD}

%description -n %{devname}
Development library for %{name}.

%prep
%setup -q

%build
sed -i 's!-Werror!!g' CMakeLists.txt
%cmake_qt5
%make

%install
%makeinstall_std -C build

%files -n %{libname}
%{_libdir}/lib*Papyros.so.%{major}*

%files -n %{devname}
%dir %{_includedir}/Papyros
%dir %{_includedir}/Papyros/Papyros
%dir %{_includedir}/Papyros/papyros
%dir %{_libdir}/cmake/Papyros
%{_includedir}/Papyros/Papyros/KQuickConfig
%{_includedir}/Papyros/Papyros/QQuickList
%{_includedir}/Papyros/Papyros/QObjectListModel
%{_includedir}/Papyros/papyros/*.h
%{_libdir}/cmake/Papyros/*.cmake
%{_libdir}/lib*Papyros.so
