%define debug_package %nil
%define snap %nil

Summary:	Papyros Libraries
Name:		libpapyros
Version:	0.1.0
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

%prep
%setup -q

%build
%cmake_qt5
%ninja

%install
%ninja_install -C build

%files
