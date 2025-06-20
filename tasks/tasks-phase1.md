# Phase 1 Tasks

## Authentication
- [ ] Design `User` SQLAlchemy model with hashed password field
- [ ] Create migration or schema update for users table
- [ ] Implement registration endpoint
- [ ] Implement login endpoint returning JWT token
- [ ] Apply auth dependency to posts routes
- [ ] Write unit tests for sign-up and login flows

## Social Features
- [ ] Add `Like` model and like/unlike endpoints
- [ ] Add `Comment` model and CRUD endpoints
- [ ] Implement notification table for new likes/comments
- [ ] Provide endpoint to fetch notifications
- [ ] Test likes, comments and notifications

## Real-time Updates
- [ ] Create WebSocket endpoint for live feed
- [ ] Broadcast new posts and notifications via WebSocket
- [ ] Implement simple WebSocket client in frontend
- [ ] Integration tests for WebSocket events

## Documentation & DevOps
- [ ] Document new API routes and authentication flow
- [ ] Update Docker Compose services for added dependencies
- [ ] Extend README with instructions for running Phase 1 features

