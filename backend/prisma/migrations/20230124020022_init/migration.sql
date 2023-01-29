/*
  Warnings:

  - You are about to drop the `FollowsCustomer` table. If the table is not empty, all the data it contains will be lost.

*/
-- DropForeignKey
ALTER TABLE "FollowsCustomer" DROP CONSTRAINT "FollowsCustomer_followerId_fkey";

-- DropForeignKey
ALTER TABLE "FollowsCustomer" DROP CONSTRAINT "FollowsCustomer_followingId_fkey";

-- DropTable
DROP TABLE "FollowsCustomer";

-- CreateTable
CREATE TABLE "CustomerFollowsCustomer" (
    "followerId" INTEGER NOT NULL,
    "followingId" INTEGER NOT NULL,

    CONSTRAINT "CustomerFollowsCustomer_pkey" PRIMARY KEY ("followerId","followingId")
);

-- AddForeignKey
ALTER TABLE "CustomerFollowsCustomer" ADD CONSTRAINT "CustomerFollowsCustomer_followerId_fkey" FOREIGN KEY ("followerId") REFERENCES "Customer"("id") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "CustomerFollowsCustomer" ADD CONSTRAINT "CustomerFollowsCustomer_followingId_fkey" FOREIGN KEY ("followingId") REFERENCES "Customer"("id") ON DELETE RESTRICT ON UPDATE CASCADE;
