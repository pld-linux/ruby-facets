%define tarname facets
Summary:	Ruby's Fantasic Atomic Core Extensions
Summary(pl):	Ruby's Fantasic Atomic Core Extensions - biblioteka rozszerzeñ
Name:		ruby-facets
Version:	2005.10.30
Release:	1
License:	Ruby-alike
Group:		Development/Languages
Source0:	http://rubyforge.org/frs/download.php/6807/%{tarname}-%{version}.tar.bz2
# Source0-md5:	a87fe15334eb5294aaefa23f38a37591
URL:		http://facets.rubyforge.org/
BuildRequires:	rpmbuild(macros) >= 1.263
BuildRequires:	ruby
Requires:	ruby
Obsoletes:	ruby-nano
Obsoletes:	ruby-mega
#BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Ruby's Fantasic Atomic Core Extensions. It is named so, because the
most unique aspect of this library is the atomicity of its extensions
layout. Every extension method is kept in it's own file, so it can be
required independently. But this is only half of what Facets offers.
Facets also includes a vast higher-level collection of classes,
modules, mixins and other assorted additions. Examples include an
ordered hash, module macros for dynamic mixins, attribute casters,
etc.

%description -l pl
Pakiet Ruby's Fantasic Atomic Core Extensions - ma tak± nazwê,
poniewa¿ najbardziej unikalny aspekt tej biblioteki to atomowo¶æ w
uk³adzie rozszerzeñ. Ka¿da metoda rozszerzenia jest przechowywana w
oddzielnym pliku, który mo¿e byæ wymagany niezale¿nie. Ale to tylko
po³owa tego, co oferuje Facets. Facets zawiera tak¿e obszern± kolekcjê
klas, modu³ów, mixinów i innych dodatków wy¿szego poziomu. Przyk³ady
obejmuj± uporz±dkowane hasze, makra modu³ów dla dynamicznych mixinów,
rzutowanie atrybutów itp.

%prep
%setup -q -n %{tarname}-%{version}

%build
rdoc --ri --op ri lib
rdoc --op rdoc lib

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_rubylibdir},%{ruby_ridir},%{_examplesdir}/%{name}-%{version}}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_rubylibdir}
cp -a ri/ri/* $RPM_BUILD_ROOT%{ruby_ridir}
cp -a demo/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc rdoc README
%{ruby_rubylibdir}/*
#%{ruby_ridir}/*
%{_examplesdir}/%{name}-%{version}
