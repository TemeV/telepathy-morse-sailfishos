Name:       telepathy-morse
Summary:    Telepathy connection manager for Telegram
Version:    0.1.0
Release:    1
Group:      Qt/Qt
License:    LICENSE
URL:        https://github.com/TelepathyQt/telepathy-morse
Source0:    %{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(telepathy-qt5) >= 0.9.6.1
BuildRequires:  telegram-qt5

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

