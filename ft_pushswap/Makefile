NAME		= push_swap
CC			= cc
CFLAGS		= -Wall -Wextra -Werror

LIBFT       = ./libft/libft.a

SRCS		= main.c \
			  init.c \
			  init_utils.c \
			  init_target.c \
			  turk.c \
			  list_utils.c \
			  atoil.c \
			  push.c \
			  swap.c \
			  rotate.c \
			  rev_rotate.c

OBJS		= $(SRCS:.c=.o)

all: $(NAME)

$(LIBFT):
	make -C ./libft/

$(NAME): $(LIBFT) $(OBJS)
	$(CC) $(CFLAGS) $(OBJS) $(LIBFT) -o $(NAME)


%.o: %.c
	$(CC) $(CFLAGS) -c $< -o $@

clean:
	rm -f $(OBJS)
	make -C ./libft clean

fclean: clean
	rm -f $(NAME)
	make -C ./libft fclean

re: fclean all

.PHONY: all clean fclean re
