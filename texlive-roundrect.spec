%global tl_name roundrect
%global tl_revision 39796

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.2
Release:	%{tl_revision}.1
Summary:	MetaPost macros for highly configurable rounded rectangles (optionally with t...
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/metapost/contrib/macros/roundrect
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/roundrect.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/roundrect.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/roundrect.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The roundrect macros for MetaPost provide ways to produce rounded
rectangles, which may or may not contain a title bar or text (the title
bar may itself contain text). They are extremely configurable.

