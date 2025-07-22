/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strcapitalize.c                                 :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mboubaza <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/07/20 05:15:51 by mboubaza          #+#    #+#             */
/*   Updated: 2025/07/21 22:20:38 by mboubaza         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

static int	is_lower(char c)
{
	return (c >= 'a' && c <= 'z');
}

static int	is_upper(char c)
{
	return (c >= 'A' && c <= 'Z');
}

static int	is_letter(char c)
{
	return (is_lower(c) || is_upper(c));
}

static void	sw_case(char *c)
{
	if (is_upper(*c))
		*c = *c + ('a' - 'A');
	else if (is_lower(*c))
		*c = *c - ('a' - 'A');
}

char	*ft_strcapitalize(char *str)
{
	int	i;

	i = 1;
	if (is_lower(str[0]))
		sw_case(&str[0]);
	while (str[i] != '\0')
	{
		if (!((str[i - 1] >= '0' && str[i - 1] <= '9')
				|| is_letter(str[i - 1])))
		{
			if (is_lower(str[i]))
				sw_case(&str[i]);
		}
		else if (is_upper(str[i]))
		{
			sw_case(&str[i]);
		}
		i++;
	}
	return (str);
}
