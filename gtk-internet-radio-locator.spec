Name:           gnome-radio
Version:        264.0
Release:        1%{?dist}
Summary:        Internet Radio Locator for GTK 4
License:        GPLv3+
URL:            http://www.gnomeradio.org/~ole/radio/
Source:         %{url}/%{name}-%{version}.tar.xz

BuildRequires:  gtk4-devel
BuildRequires:  pango
BuildRequires:  libchamplain-devel
BuildRequires:  libxml2-devel
BuildRequires:  intltool
BuildRequires:  itstool
BuildRequires:  libappstream-glib
BuildRequires:  desktop-file-utils
BuildRequires:  geocode-glib-devel
BuildRequires:  gstreamer1-devel
BuildRequires:  gstreamer1-plugins-bad-free-devel
BuildRequires:  gstreamer1-plugins-base-devel
Requires:       gstreamer1 >= 1.8.3
Requires:       gstreamer1-plugins-ugly-free >= 1.8.3
Requires:       geocode-glib >= 3.20.1

%description
Internet Radio Locator for GTK is a Free Software program
that allows you to easily locate and listen to Free Internet Radio
stations by broadcasters on the Internet with the help of a map.

Internet Radio Locator for GTK is developed on for the brand
new GTK platform and it requires gstreamer 1.0 for playback.

Enjoy Free Internet Radio.

%prep
%setup -q

%build
%configure --with-recording --disable-silent-rules --disable-schemas

%install
%make_install
%find_lang %{name} --with-man

%check
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/appdata/%{name}.appdata.xml
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop
%post
%files -f %{name}.lang
%doc AUTHORS DEBIAN NEWS README TODO ChangeLog
%license COPYING
%{_bindir}/%{name}
%{_bindir}/gtk-internet-radio-locator
%{_datadir}/%{name}/
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_mandir}/man1/%{name}.1*
%{_datadir}/icons/hicolor/1024x1024/apps/gtk-internet-radio-locator.png
%{_datadir}/icons/hicolor/16x16/apps/gtk-internet-radio-locator.png
%{_datadir}/icons/hicolor/22x22/apps/gtk-internet-radio-locator.png
%{_datadir}/icons/hicolor/24x24/apps/gtk-internet-radio-locator.png
%{_datadir}/icons/hicolor/256x256/apps/gtk-internet-radio-locator.png
%{_datadir}/icons/hicolor/32x32/apps/gtk-internet-radio-locator.png
%{_datadir}/icons/hicolor/48x48/apps/gtk-internet-radio-locator.png
%{_datadir}/icons/hicolor/512x512/apps/gtk-internet-radio-locator.png

%changelog
* Wed Jan 17 2024 Ole Aamot <ole@aamot.org> - 128.0-1
* gtk-internet-radio-locator 264.0 build on Fedora Linux 40

* Fri Nov 10 2023 Ole Aamot <ole@aamot.org> - 128.0-1
- gtk-internet-radio-locator 128.0 build on Fedora Linux 39

* Fri Nov 03 2023 Ole Aamot <ole@aamot.org> - 5.0.1-1
- gtk-internet-radio-locator 5.0.1 build on Fedora Linux 39

* Tue Nov 22 2022 Ole Aamot <ole@gnome.org> - 4.9.2-1
- gtk-internet-radio-locator 4.9.2 build on Fedora Linux 38

* Tue Nov 22 2022 Ole Aamot <ole@gnome.org> - 0.0.4-1
- gtk-internet-radio-locator 0.0.4 build on Fedora Linux 38

* Wed May 30 2018 Ole Aamot <ole@gnome.org> - 0.0.2-1
- gtk-internet-radio-locator 0.0.2 build on Fedora Linux 28

* Tue May 29 2018 Ole Aamot <ole@gnome.org> - 0.0.1-1
- gtk-internet-radio-locator 0.0.1 build on Fedora Linux 28
