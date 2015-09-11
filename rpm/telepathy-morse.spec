Name:       telepathy-morse

# >> macros
# << macros

Summary:    Telepathy connection manager for Telegram
Version:    0.1.0
Release:    1
Group:      Qt/Qt
License:    LICENSE
URL:        https://github.com/TelepathyQt/telepathy-morse
Source0:    %{name}-%{version}.tar.bz2
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(telepathy-qt5) >= 0.9.6.1
BuildRequires:  telegram-qt5

%description
Telepathy connection manager for Telegram

%prep
%setup -q -n %{name}-%{version}/telepathy-morse

# >> setup
# << setup

%build
# >> build pre
# << build pre

%cmake
make %{?_smp_mflags}

# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%make_install

# >> install post
# << install post

%files
%defattr(-,root,root,-)
%{_libdir}exec/
%{_datadir}/telepathy/managers/
%{_datadir}/dbus-1/services
# >> files
# << files
