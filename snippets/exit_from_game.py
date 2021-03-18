def exit_from_game():
    "We're closing this game"

    if event.type == pygame.QUIT or (
        event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
        # exit()
        pygame.quit()
        sys.exit()


