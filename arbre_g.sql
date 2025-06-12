-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1
-- Généré le : jeu. 12 juin 2025 à 21:56
-- Version du serveur : 10.4.32-MariaDB
-- Version de PHP : 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `arbre_g`
--

-- --------------------------------------------------------

--
-- Structure de la table `cousine_1_cousin_1`
--

CREATE TABLE `cousine_1_cousin_1` (
  `id_cousine1_cousin1` int(11) NOT NULL,
  `nom` text NOT NULL,
  `age` int(11) NOT NULL,
  `infos` text NOT NULL,
  `avatar` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `cousine_1_cousin_1`
--

INSERT INTO `cousine_1_cousin_1` (`id_cousine1_cousin1`, `nom`, `age`, `infos`, `avatar`) VALUES
(1, 'Echa', 12, 'Fille de Felana et Tambou', 'avatar_fille_2.png'),
(2, 'Iliman', 6, 'Fils de Felana et Tambou', 'avatar_boy.png');

-- --------------------------------------------------------

--
-- Structure de la table `cousine_2_3`
--

CREATE TABLE `cousine_2_3` (
  `id_cousine_2_3` int(11) NOT NULL,
  `nom` text NOT NULL,
  `age` int(11) NOT NULL,
  `infos` text NOT NULL,
  `avatar` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `cousine_2_3`
--

INSERT INTO `cousine_2_3` (`id_cousine_2_3`, `nom`, `age`, `infos`, `avatar`) VALUES
(1, 'Dinot', 18, 'Fils de Niry et Parally', 'avatar_boy.png'),
(2, 'Cheria', 21, 'Fille de Niry et Parally', 'avatar_fille_1.png');

-- --------------------------------------------------------

--
-- Structure de la table `grand_parents`
--

CREATE TABLE `grand_parents` (
  `id_grand_parents` int(11) NOT NULL,
  `nom` text NOT NULL,
  `age` int(11) NOT NULL,
  `infos` text NOT NULL,
  `avatar` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `grand_parents`
--

INSERT INTO `grand_parents` (`id_grand_parents`, `nom`, `age`, `infos`, `avatar`) VALUES
(1, 'Mariette', 78, 'Mère de Mana', 'avatar_mere.png'),
(2, 'Motherland', 80, 'Père de Mana', 'avatar_homme.png');

-- --------------------------------------------------------

--
-- Structure de la table `moi_et_ma_soeur`
--

CREATE TABLE `moi_et_ma_soeur` (
  `id_moi_ma_soeur` int(11) NOT NULL,
  `nom` text NOT NULL,
  `age` int(11) NOT NULL,
  `infos` text NOT NULL,
  `avatar` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `moi_et_ma_soeur`
--

INSERT INTO `moi_et_ma_soeur` (`id_moi_ma_soeur`, `nom`, `age`, `infos`, `avatar`) VALUES
(1, 'Zidane', 22, 'Fils de Mana et Sidonie', 'avatar_boy.png'),
(2, 'Juana', 18, 'Fille de Mana et Sidonie', 'avatar_fille_2.png');

-- --------------------------------------------------------

--
-- Structure de la table `oncle1_tante1`
--

CREATE TABLE `oncle1_tante1` (
  `id_oncle1_tante1` int(11) NOT NULL,
  `nom` text NOT NULL,
  `age` int(11) NOT NULL,
  `infos` text NOT NULL,
  `avatar` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `oncle1_tante1`
--

INSERT INTO `oncle1_tante1` (`id_oncle1_tante1`, `nom`, `age`, `infos`, `avatar`) VALUES
(1, 'Tambou', 47, 'Père de Echa et Iliman', 'avatar_homme.png'),
(2, 'Felana', 45, 'Mère de Echa et Iliman', 'avatar_mere_2.png');

-- --------------------------------------------------------

--
-- Structure de la table `oncle2_tante2`
--

CREATE TABLE `oncle2_tante2` (
  `id_oncle2_tante2` int(11) NOT NULL,
  `nom` text NOT NULL,
  `age` int(11) NOT NULL,
  `infos` text NOT NULL,
  `avatar` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `oncle2_tante2`
--

INSERT INTO `oncle2_tante2` (`id_oncle2_tante2`, `nom`, `age`, `infos`, `avatar`) VALUES
(1, 'Parally', 53, 'Père de Dinot et Cheria', 'avatar_homme.png'),
(2, 'Niry', 50, 'Mère de Dinot et Cheria', 'avatar_mere.png');

-- --------------------------------------------------------

--
-- Structure de la table `parents`
--

CREATE TABLE `parents` (
  `id_parents` int(11) NOT NULL,
  `nom` text NOT NULL,
  `age` int(11) NOT NULL,
  `infos` text NOT NULL,
  `avatar` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `parents`
--

INSERT INTO `parents` (`id_parents`, `nom`, `age`, `infos`, `avatar`) VALUES
(1, 'Mana Thomas', 52, 'Père de Zidane et Juana', 'avatar_homme.png'),
(2, 'Sidonie', 48, 'Mère de Zidane et Juana', 'avatar_mere.png');

-- --------------------------------------------------------

--
-- Structure de la table `personnes`
--

CREATE TABLE `personnes` (
  `id_personne` int(11) NOT NULL,
  `nom` varchar(255) NOT NULL,
  `age` int(11) NOT NULL,
  `infos` text NOT NULL,
  `avatar` varchar(255) DEFAULT NULL,
  `id_pere` int(11) DEFAULT NULL,
  `id_mere` int(11) DEFAULT NULL,
  `sexe` enum('homme','femme') DEFAULT NULL,
  `id_conjoint` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `personnes`
--

INSERT INTO `personnes` (`id_personne`, `nom`, `age`, `infos`, `avatar`, `id_pere`, `id_mere`, `sexe`, `id_conjoint`) VALUES
(1, 'Mariette', 78, 'Mère de Mana', 'avatar_mere.png', NULL, NULL, 'femme', 2),
(2, 'Motherland', 80, 'Père de Mana', 'avatar_homme.png', NULL, NULL, 'homme', 1),
(3, 'Mana Thomas', 52, 'Père de Zidane et Juana', 'avatar_homme.png', 2, 1, 'homme', 4),
(4, 'Sidonie', 48, 'Mère de Zidane et Juana', 'avatar_mere.png', NULL, NULL, 'femme', 3),
(5, 'Zidane', 22, 'Fils de Mana et Sidonie', 'avatar_boy.png', 3, 4, 'homme', NULL),
(6, 'Juana', 18, 'Fille de Mana et Sidonie', 'avatar_fille_2.png', 3, 4, 'femme', NULL),
(7, 'Tambou', 47, 'Père de Echa et Iliman', 'avatar_homme.png', 2, 1, 'homme', 8),
(8, 'Felana', 45, 'Mère de Echa et Iliman', 'avatar_mere_2.png', 2, 1, 'femme', 7),
(9, 'Echa', 12, 'Fille de Felana et Tambou', 'avatar_fille_2.png', 7, 8, 'femme', NULL),
(10, 'Iliman', 6, 'Fils de Felana et Tambou', 'avatar_boy.png', 7, 8, 'homme', NULL),
(11, 'Parally', 53, 'Père de Dinot et Cheria', 'avatar_homme.png', 2, 1, 'homme', 12),
(12, 'Niry', 50, 'Mère de Dinot et Cheria', 'avatar_mere.png', 2, 1, 'femme', 11),
(13, 'Dinot', 18, 'Fils de Niry et Parally', 'avatar_boy.png', 11, 12, 'homme', NULL),
(14, 'Cheria', 21, 'Fille de Niry et Parally', 'avatar_fille_1.png', 11, 12, 'femme', NULL);

-- --------------------------------------------------------

--
-- Structure de la table `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `nom` varchar(200) NOT NULL,
  `prenom` varchar(200) NOT NULL,
  `mot_de_passe` varchar(200) NOT NULL,
  `infos` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `users`
--

INSERT INTO `users` (`id`, `nom`, `prenom`, `mot_de_passe`, `infos`) VALUES
(1, 'zida', 'dane', 'lala', '');

--
-- Index pour les tables déchargées
--

--
-- Index pour la table `cousine_1_cousin_1`
--
ALTER TABLE `cousine_1_cousin_1`
  ADD PRIMARY KEY (`id_cousine1_cousin1`);

--
-- Index pour la table `cousine_2_3`
--
ALTER TABLE `cousine_2_3`
  ADD PRIMARY KEY (`id_cousine_2_3`);

--
-- Index pour la table `grand_parents`
--
ALTER TABLE `grand_parents`
  ADD PRIMARY KEY (`id_grand_parents`);

--
-- Index pour la table `moi_et_ma_soeur`
--
ALTER TABLE `moi_et_ma_soeur`
  ADD PRIMARY KEY (`id_moi_ma_soeur`);

--
-- Index pour la table `oncle1_tante1`
--
ALTER TABLE `oncle1_tante1`
  ADD PRIMARY KEY (`id_oncle1_tante1`);

--
-- Index pour la table `oncle2_tante2`
--
ALTER TABLE `oncle2_tante2`
  ADD PRIMARY KEY (`id_oncle2_tante2`);

--
-- Index pour la table `parents`
--
ALTER TABLE `parents`
  ADD PRIMARY KEY (`id_parents`);

--
-- Index pour la table `personnes`
--
ALTER TABLE `personnes`
  ADD PRIMARY KEY (`id_personne`),
  ADD KEY `id_pere` (`id_pere`),
  ADD KEY `id_mere` (`id_mere`);

--
-- Index pour la table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT pour les tables déchargées
--

--
-- AUTO_INCREMENT pour la table `cousine_1_cousin_1`
--
ALTER TABLE `cousine_1_cousin_1`
  MODIFY `id_cousine1_cousin1` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT pour la table `cousine_2_3`
--
ALTER TABLE `cousine_2_3`
  MODIFY `id_cousine_2_3` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT pour la table `grand_parents`
--
ALTER TABLE `grand_parents`
  MODIFY `id_grand_parents` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT pour la table `moi_et_ma_soeur`
--
ALTER TABLE `moi_et_ma_soeur`
  MODIFY `id_moi_ma_soeur` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT pour la table `oncle1_tante1`
--
ALTER TABLE `oncle1_tante1`
  MODIFY `id_oncle1_tante1` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT pour la table `oncle2_tante2`
--
ALTER TABLE `oncle2_tante2`
  MODIFY `id_oncle2_tante2` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT pour la table `parents`
--
ALTER TABLE `parents`
  MODIFY `id_parents` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT pour la table `personnes`
--
ALTER TABLE `personnes`
  MODIFY `id_personne` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- AUTO_INCREMENT pour la table `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- Contraintes pour les tables déchargées
--

--
-- Contraintes pour la table `personnes`
--
ALTER TABLE `personnes`
  ADD CONSTRAINT `personnes_ibfk_1` FOREIGN KEY (`id_pere`) REFERENCES `personnes` (`id_personne`) ON DELETE SET NULL,
  ADD CONSTRAINT `personnes_ibfk_2` FOREIGN KEY (`id_mere`) REFERENCES `personnes` (`id_personne`) ON DELETE SET NULL;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
