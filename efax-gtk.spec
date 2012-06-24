Summary:	Efax-gtk - a GUI front end for the 'efax' fax program
Summary(pl):	Efax-gtk - graficzny interfejs do programu 'efax'
Name:		efax-gtk
Version:	3.0.9
Release:	1
License:	GPL
Group:		Applications/Communications
Source0:	http://dl.sourceforge.net/efax-gtk/%{name}-%{version}.src.tgz
# Source0-md5:	15a0dd6f3c12e1fdcd1ffcbb902314f6
Patch0:		%{name}-desktop.patch
URL:		http://efax-gtk.sourceforge.net/
BuildRequires:	gtk+2-devel >= 2.0.0
BuildRequires:	libsigc++-devel >= 1.2.3
BuildRequires:	pkgconfig >= 1:0.9.0
Requires:	ghostscript
Conflicts:	efax
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Efax-gtk is a GUI front end for the 'efax' fax program. It can be used
to send and receive faxes with a fax modem, and to view, print and
manage faxes received. It also has a socket interface to provide a
"virtual printer" for sending faxes from word processors and similar
programs, and can automatically e-mail a received fax to a designated
user, and automatically print a received fax. This is a program to
send and receive faxes over class 1 or class 2 fax modems. It has a
nice interface to help facilitate faxing.

%description -l pl
Efax-gtk jest graficznym interfejsem prorgamu 'efax'. Mo�e by� u�ywany
do wysy�ania i odbierania faks�w z fax-modemu, oraz do ogl�dania i
drukowania odebranych faks�w. Ma tak�e interfejs w postaci gniazda
udost�pniaj�cy "wirtualn� drukark�" do wysy�ania faks�w z procesor�w
tekstu i podobnych program�w, a tak�e mo�e automatycznie wysy�a�
otrzymane faksy poczt� elektroniczn� do okre�lonego u�ytkownika i
automatycznie drukowa� otrzymane faksy. Ten program mo�e wysy�a� i
odbiera� faksy przy u�yciu fax-modem�w klasy 1 i 2. Ma przyjemny
interfejs u�atwiaj�cy faksowanie.

%prep
%setup -q
%patch0 -p1

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

ln -s %{_bindir}/efax-0.9a $RPM_BUILD_ROOT%{_bindir}/efax
ln -s %{_bindir}/efix-0.9a $RPM_BUILD_ROOT%{_bindir}/efix

%find_lang %{name}
%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/efax-gtkrc
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/%{name}.desktop
%{_mandir}/man1/*
%dir /var/spool/fax
/var/spool/fax/efax-gtk-faxfilter
/var/spool/fax/efax-gtk-socket-client
