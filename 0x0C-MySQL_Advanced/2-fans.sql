-- ranks country origins of bands, ordered by the number of (non-unique) fans
-- number of fans by country
SELECT origin,
	SUM(fans) as nb_fans
FROM metal_bands
group by origin
order by nb_fans DESC;