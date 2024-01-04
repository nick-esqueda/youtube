from .db import db
from .video_like import video_like
from .video_dislike import video_dislike
from sqlalchemy.sql import func


class Video(db.Model):
    __tablename__ = "videos"

    id = db.Column(db.Integer, primary_key=True)
    channelId = db.Column(db.Integer, db.ForeignKey("channels.id"), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(50000), nullable=True)
    videoUrl = db.Column(db.String(255), nullable=False)
    thumbnailUrl = db.Column(db.String(255), nullable=False)
    createdAt = db.Column(
        db.DateTime(timezone=True), server_default=func.now(), nullable=False
    )
    updatedAt = db.Column(
        db.DateTime(timezone=True),
        server_onupdate=func.now(),
        server_default=func.now(),
    )

    channel = db.relationship("Channel", back_populates="videos")
    comments = db.relationship(
        "Comment", back_populates="video", lazy=True, cascade="all, delete"
    )
    likes = db.relationship(
        "Channel",
        secondary=video_like,
        back_populates="video_likes",
        lazy=True,
        cascade="all, delete",
    )
    dislikes = db.relationship(
        "Channel",
        secondary=video_dislike,
        back_populates="video_dislikes",
        lazy=True,
        cascade="all, delete",
    )

    def to_dict(self):
        return {
            "id": self.id,
            "channelId": self.channelId,
            "title": self.title,
            "description": self.description,
            "videoUrl": self.videoUrl,
            "thumbnailUrl": self.thumbnailUrl,
            "createdAt": self.createdAt,
            "channel": self.channel.to_dict_no_relations(),
            "likeCount": len(self.likes),
            "dislikeCount": len(self.dislikes),
        }

    def to_dict_no_relations(self):
        return {
            "id": self.id,
            "channelId": self.channelId,
            "title": self.title,
            "description": self.description,
            "videoUrl": self.videoUrl,
            "thumbnailUrl": self.thumbnailUrl,
            "createdAt": self.createdAt,
        }