
       collide_list = pygame.sprite.spritecollide(self, all_sprites, False)
        for sprite in collide_list:
            if sprite != self:
                if self.check_collision(sprite):
                    self.resolve_collision(sprite)
                    self.rect.move_ip(-self.velocity.x, -self.velocity.y)
                break

    def check_collision(self, other_sprite):
        axes = [self.velocity.normalize(), pygame.Vector2(-self.velocity.y, self.velocity.x).normalize()]
        for axis in axes:
            proj_self = [pygame.Vector2(corner).dot(axis) for corner in self.get_corners()]
            proj_other = [pygame.Vector2(corner).dot(axis) for corner in other_sprite.get_corners()]

            if proj_self[0] > proj_other[1] or proj_self[1] < proj_other[0]:
                return False
        return True

    def get_corners(self):
        corners = [
            self.rect.topleft,
            self.rect.topright,
            self.rect.bottomleft,
            self.rect.bottomright
        ]
        return corners

    def resolve_collision(self, other_sprite):
        relative_velocity = self.velocity - other_sprite.velocity
        collision_normal = pygame.Vector2(other_sprite.rect.center) - pygame.Vector2(self.rect.center)
        collision_normal = collision_normal.normalize()
        impulse = 2 * relative_velocity.dot(collision_normal)
        self.velocity = -self.velocity
        