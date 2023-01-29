/*
  Warnings:

  - You are about to drop the `CustomerFollowsCustomer` table. If the table is not empty, all the data it contains will be lost.
  - You are about to drop the `FollowsVendor` table. If the table is not empty, all the data it contains will be lost.
  - A unique constraint covering the columns `[userId]` on the table `Customer` will be added. If there are existing duplicate values, this will fail.
  - A unique constraint covering the columns `[userId]` on the table `Vendor` will be added. If there are existing duplicate values, this will fail.
  - Added the required column `userId` to the `Customer` table without a default value. This is not possible if the table is not empty.
  - Added the required column `userId` to the `Vendor` table without a default value. This is not possible if the table is not empty.
  - Made the column `display_name` on table `Vendor` required. This step will fail if there are existing NULL values in that column.

*/
-- CreateEnum
CREATE TYPE "UserType" AS ENUM ('VENDOR', 'CUSTOMER', 'BOTH');

-- DropForeignKey
ALTER TABLE "CustomerFollowsCustomer" DROP CONSTRAINT "CustomerFollowsCustomer_followerId_fkey";

-- DropForeignKey
ALTER TABLE "CustomerFollowsCustomer" DROP CONSTRAINT "CustomerFollowsCustomer_followingId_fkey";

-- DropForeignKey
ALTER TABLE "FollowsVendor" DROP CONSTRAINT "FollowsVendor_followerId_fkey";

-- DropForeignKey
ALTER TABLE "FollowsVendor" DROP CONSTRAINT "FollowsVendor_followingId_fkey";

-- AlterTable
ALTER TABLE "Customer" ADD COLUMN     "userId" INTEGER NOT NULL;

-- AlterTable
ALTER TABLE "Vendor" ADD COLUMN     "userId" INTEGER NOT NULL,
ALTER COLUMN "display_name" SET NOT NULL;

-- DropTable
DROP TABLE "CustomerFollowsCustomer";

-- DropTable
DROP TABLE "FollowsVendor";

-- CreateTable
CREATE TABLE "User" (
    "id" SERIAL NOT NULL,
    "createdAt" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updatedAt" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "name" TEXT,
    "display_name" TEXT,
    "full_name" TEXT,
    "active" BOOLEAN NOT NULL DEFAULT false,
    "email" TEXT NOT NULL,
    "userType" "UserType" NOT NULL DEFAULT 'CUSTOMER',

    CONSTRAINT "User_pkey" PRIMARY KEY ("id")
);

-- CreateIndex
CREATE UNIQUE INDEX "User_email_key" ON "User"("email");

-- CreateIndex
CREATE UNIQUE INDEX "Customer_userId_key" ON "Customer"("userId");

-- CreateIndex
CREATE UNIQUE INDEX "Vendor_userId_key" ON "Vendor"("userId");

-- AddForeignKey
ALTER TABLE "Vendor" ADD CONSTRAINT "Vendor_userId_fkey" FOREIGN KEY ("userId") REFERENCES "User"("id") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "Customer" ADD CONSTRAINT "Customer_userId_fkey" FOREIGN KEY ("userId") REFERENCES "User"("id") ON DELETE RESTRICT ON UPDATE CASCADE;
