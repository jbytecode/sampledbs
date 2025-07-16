# Libz for compressing and decompressing data in Julia
# StringEncodings for handling string encodings
using Libz, StringEncodings

# Sample data to compress
thedata = repeat("α β γ δ ε ζ η θ ι κ λ μ ν ξ ο π ρ σ τ υ φ χ ψ ω", 10)

# Compress the data using Libz
zippeddata = Libz.compress(read(IOBuffer(thedata)))

@info("Original data: ", thedata)

@info("Zipped data: ", zippeddata)

# Decompress the data using Libz
unzippeddata = Libz.decompress(zippeddata)

@info("Unzipped data: ", unzippeddata)

@info("Unzipped data (decoded): ", StringEncodings.decode(unzippeddata, "UTF-8"))


