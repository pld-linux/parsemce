Summary:	Linux Machine Check Exception handler parser
Summary(pl.UTF-8):	Parser dla linuksowej obsługi wyjątków Machine Check Exception
Name:		parsemce
Version:	0.0.9
Release:	1
License:	GPL
Group:		Applications/System
Source0:	http://www.codemonkey.org.uk/cruft/%{name}.c
# Source0-md5:	dc39d5001009233d15643df768015997
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Linux Machine Check Exception handler parser.

%description -l pl.UTF-8
Parser dla linuksowej obsługi wyjątków MCE (Machine Check Exception).

%prep
%setup -q -T -c

%build
%{__cc} %{rpmcflags} %{rpmldflags} %{SOURCE0} -o %{name}

%install
rm -rf $RPM_BUILD_ROOT

install -D %{name} $RPM_BUILD_ROOT%{_bindir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
