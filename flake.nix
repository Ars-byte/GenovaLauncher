{
  description = "SunshineLauncher — Minecraft Bedrock Launcher for Linux";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, flake-utils }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = nixpkgs.legacyPackages.${system};
      in
      {
        packages.default = pkgs.python3Packages.buildPythonApplication {
          pname = "sunshine-launcher";
          version = "1.0.0";
          src = self;

          propagatedBuildInputs = with pkgs.python3Packages; [
            pyside6
            pillow
          ];

          nativeBuildInputs = with pkgs; [
            qt6.full
            makeWrapper
          ];

          preFixup = ''
            makeWrapperArgs+=(
              --prefix LD_LIBRARY_PATH : ${pkgs.lib.makeLibraryPath [
                pkgs.libzip
                pkgs.xorg.libX11
                pkgs.xorg.libXext
                pkgs.libGL
                pkgs.mesa
              ]}
            )
          '';

          meta = with pkgs.lib; {
            description = "A modern Minecraft Bedrock launcher for Linux";
            homepage = "https://github.com/Ars-byte/Sunshine-launcher";
            license = licenses.gpl3;
            platforms = platforms.linux;
            maintainers = [ "Ars-byte" ];
          };
        };
      }
    );
}
