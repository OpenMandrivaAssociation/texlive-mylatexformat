%global tl_name mylatexformat
%global tl_revision 21392

Name:		texlive-%{tl_name}
Epoch:		1
Version:	3.4
Release:	%{tl_revision}.1
Summary:	Build a format based on the preamble of a LaTeX file
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/mylatexformat
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mylatexformat.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mylatexformat.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mylatexformat.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The use of formats helps to speed up compilations: packages which have
been dumped in the format are loaded at very high speed. This is useful
when a document loads many packages (including large packages such as
pgf-TikZ). The package was developed from the work in mylatex, and
eliminates many of the limitations and problems of that package.

