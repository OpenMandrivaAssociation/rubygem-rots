# Generated from rots-0.2.1.gem by gem2rpm5 -*- rpm-spec -*-          
%define	rbname	rots

Summary:	an OpenID server for making tests of OpenID clients implementations
Name:		rubygem-%{rbname}

Version:	0.2.1
Release:	2
Group:		Development/Ruby
License:	GPLv2+ or Ruby
URL:		http://github.com/roman/rots
Source0:	%{rbname}-%{version}.gem
BuildRequires:	rubygems 
BuildArch:	noarch

%description
Ruby OpenID Test Server (ROST) provides a basic OpenID server made in top of
the Rack gem.
With this small server, you can make dummy OpenID request for testing
purposes,
the success of the response will depend on a parameter given on the url of the
authentication request.

%package	doc
Summary:	Documentation for %{name}
Group:		Books/Computer books
Requires:	%{name} = %{EVRD}
BuildArch:	noarch

%description	doc
Documents, RDoc & RI documentation for %{name}.

%prep
%setup -q

%build
%gem_build -f spec/

%install
%gem_install

%files
%{_bindir}/rots
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/bin
%{ruby_gemdir}/gems/%{rbname}-%{version}/bin/rots
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/*.rb
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib/rots
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/rots/*.rb
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/spec
%{ruby_gemdir}/gems/%{rbname}-%{version}/spec/*.rb
%{ruby_gemdir}/specifications/%{rbname}-%{version}.gemspec

%files doc
%doc %{ruby_gemdir}/gems/%{rbname}-%{version}/README
%doc %{ruby_gemdir}/doc/%{rbname}-%{version}



%changelog
* Wed Feb 15 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.2.1-2
+ Revision: 774161
- mass rebuild of ruby packages against ruby 1.9.1

* Mon Oct 03 2011 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.2.1-1
+ Revision: 702544
- imported package rubygem-rots


* Mon Oct 03 2011 Per Øyvind Karlsen <peroyvind@t61.proyvind> 0.2.1-1
- Initial package
