import smbl
import snakemake
import os

import __program

ART_454      = __program.get_bin_file_path("art_454")
ART_ILLUMINA = __program.get_bin_file_path("art_illumina")
ART_SOLID    = __program.get_bin_file_path("art_solid")


##########################################
##########################################


class Art(__program.Program):
	@classmethod
	def get_installation_files(cls):
		return [
			ART_454,
			ART_ILLUMINA,
			ART_SOLID,
		]

	@classmethod
	def install(cls):
		if (smbl.is_linux() or smbl.is_cygwin()) and smbl.is_os_64bit():
			fn=cls.download_file("http://www.niehs.nih.gov/research/resources/assets/docs/artbinvanillaicecream031114linux64tgz.tgz","art.tgz")
		elif (smbl.is_linux() or smbl.is_cygwin()):
			fn=cls.download_file("http://www.niehs.nih.gov/research/resources/assets/docs/artbinvanillaicecream031114linux32tgz.tgz","art.tgz")
		elif smbl.is_mac() and smbl.is_os_64bit():
			fn=cls.download_file("http://www.niehs.nih.gov/research/resources/assets/docs/artbinvanillaicecream031114macos64tgz.tgz","art.tgz")
		elif smbl.is_mac():
			fn=cls.download_file("http://www.niehs.nih.gov/research/resources/assets/docs/artbinvanillaicecream031114macos32tgz.tgz","art.tgz")
		else:
			raise NotImplementedError("Unsupported OS")

		dir=cls.extract_tar(fn,strip=2)

		cls.install_file("art_454",ART_454)
		cls.install_file("art_illumina",ART_ILLUMINA)
		cls.install_file("art_SOLiD",ART_SOLID)

	@classmethod
	def supported_platforms(cls):
		return ["macos","linux"]
