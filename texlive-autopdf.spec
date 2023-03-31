Name:		texlive-autopdf
Version:	32377
Release:	2
Summary:	Conversion of graphics to pdfLaTeX-compatible formats
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/autopdf
License:	LPPL1.2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/autopdf.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/autopdf.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/autopdf.source.r%{version}.tar.xz
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
%doc %{_texmfdistdir}/doc/latex/autopdf/README.txt
%doc %{_texmfdistdir}/doc/latex/autopdf/autopdf.pdf
#- source
%doc %{_texmfdistdir}/source/latex/autopdf/autopdf.dtx

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
