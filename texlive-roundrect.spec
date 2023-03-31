Name:		texlive-roundrect
Version:	39796
Release:	2
Summary:	MetaPost macros for highly configurable rounded rectangles (optionally with text)
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/roundrect
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/roundrect.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/roundrect.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/roundrect.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The roundrect macros for MetaPost provide ways to produce
rounded rectangles, which may or may not contain a title bar or
text (the title bar may itself contain text). They are
extremely configurable.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/metapost/roundrect
%{_texmfdistdir}/metapost/roundrect
%doc %{_texmfdistdir}/doc/metapost/roundrect

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
