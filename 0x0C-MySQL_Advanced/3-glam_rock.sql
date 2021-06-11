-- lists all bands with Glam rock as their main style, ranked by their longevity
-- lifespan by band and style
SELECT band_name,
	ifnull(split, YEAR(CURDATE())) - formed as lifespan
FROM metal_bands
WHERE style LIKE "%Glam rock%"
ORDER BY lifespan DESC;