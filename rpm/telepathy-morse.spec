Name:       telepathy-morse
Summary:    Telepathy connection manager for Telegram
Version:    0.1.1
Release:    1
Group:      Qt/Qt
License:    LICENSE
URL:        https://github.com/TelepathyQt/telepathy-morse
Source0:    %{name}-%{version}.tar.gz
Requires:   telepathy-qt5
Requires:   telegram-qt5
BuildRequires:  cmake
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  telepathy-qt5-devel >= 0.9.7.0
BuildRequires:  telepathy-qt5-farstream-devel
BuildRequires:  telegram-qt5-devel
BuildRequires:  openssl-devel

%description
Telepathy connection manager for Telegram


%prep
%setup -q -n %{name}-%{version}/telepathy-morse


%build
%cmake
make %{?_smp_mflags}


%install
rm -rf %{buildroot}
%make_install


%files
%defattr(-,root,root,-)
%{_libdir}exec/
%{_datadir}/telepathy/managers/
%{_datadir}/dbus-1/services

