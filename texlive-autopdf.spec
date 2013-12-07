# revision 28125
# category Package
# catalog-ctan /macros/latex/contrib/autopdf
# catalog-date 2012-10-30 20:17:59 +0100
# catalog-license lppl1.2
# catalog-version 1.0
Name:		texlive-autopdf
Version:	1.0
Release:	5
Summary:	Conversion of graphics to pdfLaTeX-compatible formats
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/autopdf
License:	LPPL1.2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/autopdf.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/autopdf.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/autopdf.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package facilitates the on-the-fly conversion of various
graphics formats to formats supported by pdfLaTeX (e.g. PDF).
It uses a range of external programs, and therefore requires
that the LaTeX run starts with write18 enabled.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/autopdf/autopdf.sty
%doc %{_texmfdistdir}/doc/latex/autopdf/README
%doc %{_texmfdistdir}/doc/latex/autopdf/autopdf.pdf
#- source
%doc %{_texmfdistdir}/source/latex/autopdf/autopdf.dtx

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
