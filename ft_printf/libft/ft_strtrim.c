/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strtrim.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mboubaza <mboubaza@student.1337.ma>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/28 13:04:40 by mboubaza          #+#    #+#             */
/*   Updated: 2025/11/01 23:24:43 by mboubaza         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

static int	ft_len(char *str)
{
	int	i;

	i = 0;
	while (str[i])
		i++;
	return (i);
}

static int	is_set(char c, char *set)
{
	int	i;

	i = 0;
	while (set[i])
	{
		if (set[i] == c)
			return (1);
		i++;
	}
	return (0);
}

char	*ft_strtrim(char const *s1, char const *set)
{
	int		i;
	char	*str;
	int		beg;
	int		end;

	if (!s1 || !set)
		return (NULL);
	beg = 0;
	while (s1[beg] && is_set((char)s1[beg], (char *)set))
		beg++;
	end = ft_len((char *)s1) - 1;
	while (end >= 0 && is_set((char)s1[end], (char *)set))
		end--;
	if (end <= beg)
		return (ft_strdup(""));
	str = malloc(sizeof(char) * (end - beg + 1 + 1));
	if (!str)
		return (NULL);
	i = 0;
	while (beg <= end)
		str[i++] = (char)s1[beg++];
	str[i++] = '\0';
	return (str);
}
